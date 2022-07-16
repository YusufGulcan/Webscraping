# This code scrapes data from the biggest e-commerce retail website in Turkey. Data includes info about more than 1000 products which are suggested
# to be the most popular ones since they are located in the first 50 pages of the website search results.
import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
import re


def Trendyoldata(pagenum):  # You can specify the number of pages that you want to scrap data from.

    try:
        linklist = []  # I created bunch of lists to collect data.The lists will be later used to create the dataframe.
        Ramlist = []
        BatteryPowerlist = []
        Storagelist = []
        Screensizelist = []
        CameraResolutionlist = []
        OperatingSystemlist = []
        Colorlist = []
        CPUlist = []
        Pricelist = []
        Modellist = []
        brandlist = []

        for num in range(1, pagenum):
            # The URL is of a search result page. So the products are listed there.
            url = f'https://www.trendyol.com/akilli-cep-telefonu-x-c109460?pi={num}'  # As you scrool down the page, the url keeps changing so I created a for loop to keep up with the url.
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            Phones = soup.find_all('div', class_='p-card-wrppr')

            for each in Phones:
                link = each.find('div', class_='p-card-chldrn-cntnr').a[
                    'href']  # First I had to find the links for individual product pages in the search result page.
                link = f'https://www.trendyol.com{link}'
                linklist.append(link)
                print(link)

                response1 = requests.get(link)  # Then I created another soup for product-specific data.
                soup1 = BeautifulSoup(response1.text, 'html.parser')
                data = soup1.find('ul', class_='detail-attr-container').text




                rammatch = re.search('tesi ([1-90])',data)
                                      # I have used regular expression to catch specific data. The html tags were not built to specify each type of data.
                if rammatch:  # # They were bagged into one html anchor.
                    RAM = rammatch.group(1)
                else:
                    RAM = None
                Ramlist.append(RAM)

                Batterymatch = re.search('mAh\) ([1-90]+ - [1-90]+)', data)
                if Batterymatch:
                    BatteryPower = Batterymatch.group(1)
                else:
                    BatteryPower = None
                BatteryPowerlist.append(BatteryPower)

                Camresmatch = re.search('lüğü ([1-90]+ - [1-90]+)',
                                        data)  # I kept finding each type of data by repeating the same structure.
                if Camresmatch:
                    CameraResolution = Camresmatch.group(
                        1)  # As I collect data, I append everything to the lists I created at the beginning.
                else:
                    CameraResolution = None

                storagematch = re.search('za ([1-90]+)', data)
                if storagematch:
                    Storage = storagematch.group(1)
                else:
                    Storage = None
                Storagelist.append(Storage)

                screnesizematch = re.search('utu ([1-90]+)', data)
                screnesizematch1 = re.search('ığı ([1-90])\'\' - ([1-90].+)\'\'', data)

                if screnesizematch:
                    ScreenSize = screnesizematch.group(1)
                elif screnesizematch1:
                    ScreenSize = (float(screnesizematch1.group(1)) + float(screnesizematch1.group(2)))/2
                else:
                    ScreenSize = None
                Screensizelist.append(ScreenSize)


                Cameraresmatch = re.search('üğü ([1-90]+) MP', data)
                Cameraresmatch1 = re.search('([0-9+]+) - ([0-9]+) MPA', data)

                if Cameraresmatch:
                    CameraResolution = Cameraresmatch.group(1)
                elif Cameraresmatch1:
                    CameraResolution = (float(Cameraresmatch1.group(1)) + float(Cameraresmatch1.group(2)))/2

                else:
                    CameraResolution = None
                CameraResolutionlist.append(CameraResolution)

                Osmatch = re.search('Sistemi iOS', data)
                Osmatch1 = re.search('Sistemi Android', data)
                if Osmatch:
                    OperatingSystem = 'iOS'
                elif Osmatch1:
                    OperatingSystem = 'Android'
                else:
                    OperatingSystem = None
                print(OperatingSystem)
                print(data)

                OperatingSystemlist.append(OperatingSystem)

                colormatch = re.search('Renk ([A-Z][a-z]+)', data)
                colormatch1 = re.search('Renk ([a-zA-Z])', data)

                if colormatch:
                    Color = colormatch.group(1)
                elif colormatch1:
                    Color = colormatch1.group(1)

                else:
                    Color = None
                Colorlist.append(Color)

                Cpumatch = re.search('CPU Aralık ([1-90\.]+-[1-90\.]+)', data)
                if Cpumatch:
                    CPU = Cpumatch.group(1)
                else:
                    CPU = None
                CPUlist.append(CPU)
                print(CPU)

                price = soup1.find('span',
                                   class_='prc-dsc').text.strip()  # Price format was not compatible with the universal currency format, therefore I had to convert it
                price = price[:-2].replace('.', '')  # to an acceptable shape.
                price = price.split(',')[0]
                Pricelist.append(price)

                phonet = soup1.find('h1', class_='pr-new-br').span.text
                phonet = phonet.split(' ')
                Model = f'{phonet[1]} {phonet[2]}'
                Modellist.append(Model)
                phonet = soup1.find('div', class_='container-right-content').a.text
                if not phonet:
                    brand = None
                else:
                    brand = phonet
                brandlist.append(brand)





        specifications = {'Model': Modellist,
                          # I gathered all of my data in a dictionary and created a pandas dataframe.
                          'Brand': brandlist,
                          'Price': Pricelist,
                          'CPU': CPUlist,
                          'RAM': Ramlist,
                          'Storage': Storagelist,
                          'Operating System': OperatingSystemlist,
                          'Camera Resolution': CameraResolutionlist,
                          'Screen Size': Screensizelist,
                          'Battery Power': BatteryPowerlist,
                          'Color': Colorlist,
                          'Link': linklist
                          }

        df = pd.DataFrame(specifications)
        df.to_csv('Trendyol_detailed333.csv')  # I have written the dataframe into a csv file to be processed using the Jupyter Notebook.

    except ValueError as e:
        print(e)


Trendyoldata(50)








