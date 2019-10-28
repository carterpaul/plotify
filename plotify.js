// Sends user to login screen and redirects them to the "generate_vis" page
function authorize(){
  window.location = 'https://accounts.spotify.com/authorize' +
  '?client_id=d14bc3b1ad944237bb5d2863cc1c7790' +
  '&scope=user-library-read%20user-read-private' +
  '&response_type=token' +
  '&redirect_uri=http://localhost:8000/generate_vis.html';
}

// Calls the Spotify API to retrieve the album cover of each song in authenticated user's library
const getAlbumCovers = async()=> {
  var covers = [];
  var allSongs = {"next":'https://api.spotify.com/v1/me/tracks'};
  var access_token = getAccessToken();
  //songs are retrieved in chunks of 20, so we have to iterate through
  while(allSongs.next != null){
    var response = await fetch(allSongs.next, {
      method: 'GET',
      headers:{
        'Authorization': 'Bearer ' + access_token
      }
    });
    allSongs = await response.json(); //extract JSON from the http response
    for (var j=0; j<allSongs.items.length; j++){
      covers.push(allSongs.items[j].track.album.images[2].url);
    }
    document.getElementById('progress').innerHTML = "Fetching Songs: " +
    allSongs.offset + " / " + allSongs.total;
  }
  covers = Array.from(new Set(covers)); //remove duplicates
  drawToCanvas(covers);
};

// retrieves access token from page hash
// for use after user is redirected after logging in
function getAccessToken(){
    var url = window.location.hash; // get full page url
    var access_token = url.substring(url.indexOf("#")+14, url.indexOf("&")); // get access token from hash
    console.log("access_token: " + access_token);
    return(access_token);
}

//global variable should be changed
var coverImgs = [];

//generic load image function returns deferred promise once image is loaded
function loadImg(src){
  var deferred = $.Deferred();
  var img = new Image();
  img.onload = function(){
    deferred.resolve();
  };
  img.crossOrigin = "anonymous";
  img.src = src;
  coverImgs.push(img);
  return deferred.promise();
}

//draws images to canvas
//calls loadImg to load images
function drawToCanvas(coverURLs){
  var myCanvas = document.createElement('canvas');
  myCanvas.width = 1920;
  myCanvas.height = 1080;
  var ctx = myCanvas.getContext('2d');
  var loaders = [];
  //loads first 510 cover images
  //loads all of them if less than 510 total
  for (i=0;i<Math.min(510, coverURLs.length);i++){
    loaders.push(loadImg(coverURLs[i]));
  }
  //once all images are loaded
  $.when.apply(null, loaders).done(function() {
    for (j=0;j<coverImgs.length;j++){
      ctx.drawImage(coverImgs[j], (j%30)*64, Math.floor(j/30)*64);
    }
    //convert canvas object to png image and display it
    var collage = myCanvas.toDataURL("image/png");
    document.write('<img src="' + collage + '"/>');
    // document.createElement('image');
    // image.src = img;
    // image.crossOrigin = "Anonymous"
    // document.write(im)
  });
}
