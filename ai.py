
import boto3
import os
from PIL import Image, ImageDraw, ImageFont


class AIDetection:

    def __init__(self) -> None:
        # Bounding box implementation
        # self.arn = "arn:aws:rekognition:us-east-1:126536304024:project/AI_Basketball/version/AI_Basketball.2023-03-28T13.39.23/1680025163597"
        # Full image classification implementation
        self.arn = "arn:aws:rekognition:us-east-1:126536304024:project/AI_Basketball_FIC/version/AI_Basketball_FIC.2023-03-29T11.27.26/1680103646340"
        self.minConfidence = 80
        self.maxResults = 1
        self.client = boto3.client('rekognition')

    def setGameDirectory(self, directory: str) -> None:
        self.directory = directory

    def detectLabels(self):
        consumable = {}
        for image in os.scandir(self.directory):
            with open(image, 'rb') as raw:
                response = self.client.detect_custom_labels(Image={'Bytes': raw.read()},
                    MinConfidence=self.minConfidence,
                    MaxResults=self.maxResults,
                    ProjectVersionArn=self.arn)
                label = response['CustomLabels']
                if len(label) != 0:
                    label = label[0]
                    consumable[image.name] = f"{label['Name']} : {label['Confidence']}"
        return consumable
                
        # with open(self.testPhoto, 'rb') as image:
        #     response = self.client.detect_custom_labels(Image={'Bytes': image.read()},
        #         MinConfidence=self.minConfidence,
        #         MaxResults=self.maxResults,
        #         ProjectVersionArn=self.arn)
        
        # for label in response['CustomLabels']:
        #     print (label['Name'] + ' : ' + str(label['Confidence']))

        # return response
    

    
    def display_image(self, response: dict) -> None:
        
        image=Image.open(self.testPhoto)

        # Ready image to draw bounding boxes on it.
        imgWidth, imgHeight = image.size
        draw = ImageDraw.Draw(image)

        # calculate and display bounding boxes for each detected custom label
        print('Detected custom labels for ' + self.testPhoto)
        for customLabel in response['CustomLabels']:
            print('Label ' + str(customLabel['Name']))
            print('Confidence ' + str(customLabel['Confidence']))
            if 'Geometry' in customLabel:
                box = customLabel['Geometry']['BoundingBox']
                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']

                fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
                draw.text((left,top), customLabel['Name'], fill='#00d400', font=fnt)

                print('Left: ' + '{0:.0f}'.format(left))
                print('Top: ' + '{0:.0f}'.format(top))
                print('Label Width: ' + "{0:.0f}".format(width))
                print('Label Height: ' + "{0:.0f}".format(height))

                points = (
                    (left,top),
                    (left + width, top),
                    (left + width, top + height),
                    (left , top + height),
                    (left, top))
                draw.line(points, fill='#00d400', width=5)

        image.show()


# if __name__ == "__main__":
#     test = AIDetection()
#     response = test.detectLabels()
#     test.display_image(response)
    