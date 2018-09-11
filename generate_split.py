import glob
import re

# Get image names
filenames = glob.glob("Annotated/*png")

# Open the train, val and trainval files
train = open("train.txt", "w")
val = open("val.txt", "w")
trainval = open("trainval.txt", "w")

# Split the dataset
for name in filenames:
    # Get the image name as an integer
    name = re.findall(r'\d+', name)
    num = int(name[0])
    # Decide where each image goes
    if num % 8 == 0:
        val.write('{num:08d}'.format(num = num)+ "\n")
    else:
        train.write('{num:08d}'.format(num = num)+ "\n")
    # Also write down each image name to trainval
    trainval.write('{num:08d}'.format(num = num)+ "\n")

# Close the train, val and trainval files
train.close()
val.close()
trainval.close()
