from PIL import Image
from io import BytesIO
import requests

IMAGE_SIZE = 64
COLLAGE_WIDTH = 1920
COLLAGE_HEIGHT = 1088

# Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', action = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        action      - Optional  : current operation
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s\t\t%s' % (prefix, bar, percent, suffix, action), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

#open file and create list of urls
with open("img/covers.csv", "r") as myfile:
    urls = myfile.read().split("\n")
    del urls[-1]
    #urls = [myfile.read().split("\n")[0]]

#create a list of image
covers = []
l = len(urls)
for i, url in enumerate(urls):
    response = requests.get(url)
    covers.append(Image.open(BytesIO(response.content)))

    #print progess bar for getting image
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', action = "Getting Image", length = 50)
    
print()

#create new blank image
collage = Image.new("RGB", (COLLAGE_WIDTH, COLLAGE_HEIGHT))
i = 0
l = len(covers)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', action = "Creating Collage", length = 50)

#making the image collage
for x in range(COLLAGE_WIDTH // IMAGE_SIZE):
    for y in range(COLLAGE_HEIGHT // IMAGE_SIZE):
        if i < len(covers):
            collage.paste(covers[i], (x*IMAGE_SIZE, y*IMAGE_SIZE))
            i = i+1
            
            #print progress bar for making collage
            printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', action = "Creating Collage", length = 50)

print("\n\n")
collage.save("collage.png", "PNG")



