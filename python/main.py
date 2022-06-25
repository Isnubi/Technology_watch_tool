# coding: utf-8
# import libraries
import unicodedata
import requests
from bs4 import BeautifulSoup
import csv
import ftplib
from datetime import datetime
from deep_translator import GoogleTranslator
# import ftp server information
import config


def time():
    """
    Return the current time in the format dd/mm/YYYY HH:MM:SS
    """
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    print("====================")
    print(current_time)


def login_ftp(ftpinstance):
    """
    Connect to the FTP server
    :param ftpinstance:
    """
    host = config.ftp_host
    port = 21
    ftpinstance.connect(host, port)
    print(ftpinstance.getwelcome())
    try:
        print("Logging in ...")
        ftpinstance.login(config.ftp_login, config.ftp_password)
        print("Logged")
    except ftplib.all_errors:
        print("Failed to login")


def send_ftp(local_path, ftp_dir, ftp_file):
    """
    Send the file to the FTP server
    :param local_path: the local path of the file
    :param ftp_dir: the directory on the FTP server
    :param ftp_file: the name of the file on the FTP server
    """
    print("====================")
    login_ftp(logftp)
    logftp.cwd(ftp_dir)
    with open(local_path, "rb") as f:
        try:
            logftp.storbinary(ftp_file, f)
            print("File " + ftp_file + " send")
        except:
            print("Failed to send the file")
    logftp.close()
    print("Disconnected")


def lmi_parser_articles(webpath):
    """
    Parse the articles on the website lemondeinformatique.fr
    :param webpath: the path of the website
    """
    page = requests.get(webpath)
    soup = BeautifulSoup(page.content, 'html.parser')
    web_array = soup.find_all("article", class_="item")
    return web_array


def lmi_csv_creation(csv_path, csv_array):
    """
    Create a CSV file with the articles of the website lemondeinformatique.fr
    :param csv_path: the path of the CSV file
    :param csv_array: the array of the articles
    """
    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for obj in csv_array:
            div_img = obj.find("div", class_="col-sm-4 col-xs-5")
            div_link = obj.find("div", class_="col-sm-8 col-xs-7")
            img = div_img.find("noscript")
            img_div = img.find(src=True)
            img_link = img_div['src']
            link = div_link.find(href=True)
            lien = link['href']
            title = div_link.find("a", class_="title")
            date = div_link.find("b")
            try:
                titre = ''.join((c for c in unicodedata .normalize('NFD', title.string) if unicodedata.category(c) != 'Mn'))
            except TypeError:
                continue
            ligne = [titre, lien, date.string, img_link]
            writer.writerow(ligne)


def silicon_parser_articles(webpath):  # Specific parser for silicon.fr
    """
    Parse the articles on the website silicon.fr
    :param webpath: the path of the website
    """
    page = requests.get(webpath)
    soup = BeautifulSoup(page.content, 'html.parser')
    web_array = soup.find_all("article")
    return web_array


def silicon_csv_creation(csv_path, csv_array):
    """
    Create a CSV file with the articles of the website silicon.fr
    :param csv_path: the path of the CSV file
    :param csv_array: the array of the articles
    """
    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for obj in csv_array:
            div_link = obj.find("h2", class_="entry-title")
            link = div_link.find(href=True)
            lien = link['href']
            div_title = obj.find("h2", class_="entry-title")
            title_div = div_title.find(title=True)
            title = title_div['title']
            div_img = obj.find("img")
            img = div_img['data-src']
            try:
                titre = ''.join((c for c in unicodedata .normalize('NFD', title) if unicodedata.category(c) != 'Mn'))
            except TypeError:
                continue
            ligne = [titre, lien, img]
            writer.writerow(ligne)


def vladan_parser_articles(webpath):
    """
    Parse the articles on the website vladan.fr
    :param webpath: the path of the website
    """
    page = requests.get(webpath)
    soup = BeautifulSoup(page.content, 'html.parser')
    web_array = soup.find_all("article")
    return web_array


def vladan_csv_creation(csv_path, csv_array):
    """
    Create a CSV file with the articles of the website vladan.fr
    :param csv_path: the path of the CSV file
    :param csv_array: the array of the articles
    """
    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for obj in csv_array:
            div_header = obj.find("h2", class_="entry-title")
            link = div_header.find(href=True)
            lien = link['href']
            title = div_header.string

            div_date = obj.find("p", class_="entry-meta")
            date_div = div_date.find("time", class_="entry-time")
            date_fr = GoogleTranslator(source='english', target='french').translate(date_div.string)

            div_img = obj.find("noscript")
            img = div_img.find(src=True)
            img_link = img['src']

            try:
                titre = ''.join((c for c in unicodedata .normalize('NFD', title.string) if unicodedata.category(c) != 'Mn'))
                date = ''.join((c for c in unicodedata.normalize('NFD', date_fr) if unicodedata.category(c) != 'Mn'))
            except TypeError:
                continue
            ligne = [titre, lien, date, img_link]
            writer.writerow(ligne)


def ud_parser_articles(webpath):
    """
    Parse the articles on the website usine-digitale.fr
    :param webpath: the path of the website
    """
    page = requests.get(webpath)
    soup = BeautifulSoup(page.content, 'html.parser')
    web_array = soup.find_all("section", class_="blocType2")
    return web_array


def ud_csv_creation(csv_path, csv_array):
    """
    Create a CSV file with the articles of the website usine-digitale.fr
    :param csv_path: the path of the CSV file
    :param csv_array: the array of the articles
    """
    with open(csv_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for obj in csv_array:
            div_link = obj.find("a", class_="contenu", href=True)
            lien = div_link['href']

            div_title = obj.find("h2", class_="titreType2")
            title = div_title.string

            div_img = obj.find("img", src=True)
            img_path = div_img['src']
            img = "https://www.usine-digitale.fr" + img_path

            date_div = obj.find("span", class_="dateEtiquette2")
            date = date_div.string[0:10]

            try:
                titre = ''.join((c for c in unicodedata .normalize('NFD', title) if unicodedata.category(c) != 'Mn'))
            except TypeError:
                continue
            ligne = [titre, lien, date, img]
            writer.writerow(ligne)


def start_parse(url, website, topic):
    """
    Function to clean code and launch all the functions (parser, FTP, CSV creation)
    :param url: the url of the website
    :param website: the name of the website
    :param topic: the topic of the website
    """
    path = "/root/csv/"  + topic + "_" + website + ".csv"
    prefix = topic + "_" + website
    outputfile = "STOR " + prefix + ".csv"
    parse = website + "_parser_articles"
    articles = globals()[parse](url)
    csv = website + "_csv_creation"
    globals()[csv](path, articles)
    send_ftp(path, outputdir, outputfile)


outputdir = "/www/csv/"
logftp = ftplib.FTP()
time()

# ---------------------- Parsage lemondeinformatique.fr ----------------------

start_parse("https://www.lemondeinformatique.fr/securite-informatique-3.html", "lmi", "securite")
start_parse("https://www.lemondeinformatique.fr/reseaux-197.html", "lmi", "securite_reseau")
start_parse("https://www.lemondeinformatique.fr/serveurs-198.html", "lmi", "securite_serveur")
start_parse("https://www.lemondeinformatique.fr/malware-34.html", "lmi", "malware")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-marque-sur-anssi-331.html", "lmi", "anssi")

start_parse("https://www.lemondeinformatique.fr/virtualisation-informatique-7.html", "lmi", "virtualisation")
start_parse("https://www.lemondeinformatique.fr/virtualisation-de-reseau-77.html", "lmi", "virtualisation_reseau")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-marque-sur-vmware-18.html", "lmi", "vmware")
start_parse("https://www.lemondeinformatique.fr/conteneur-148.html", "lmi", "conteneur")

start_parse("https://www.lemondeinformatique.fr/datacenter-5.html", "lmi", "datacenter")
start_parse("https://www.lemondeinformatique.fr/virtualisation-informatique-54.html", "lmi", "datacenter_virtualisation")
start_parse("https://www.lemondeinformatique.fr/green-it-50.html", "lmi", "datacenter_greenit")
start_parse("https://www.lemondeinformatique.fr/innovations-technologiques-56.html", "lmi", "datacenter_innovation")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-produit-sur-aws-70.html", "lmi", "aws")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-produit-sur-azure-28.html", "lmi", "azure")

start_parse("https://www.lemondeinformatique.fr/hardware-et-materiel-informatique-9.html", "lmi", "hardware")
start_parse("https://www.lemondeinformatique.fr/serveur-informatique-94.html", "lmi", "hardware_serveur")
start_parse("https://www.lemondeinformatique.fr/hyperconvergence-147.html", "lmi", "hyperconvergence")

start_parse("https://www.lemondeinformatique.fr/systeme-d-exploitation-windows-macos-linux-10.html", "lmi", "os")
start_parse("https://www.lemondeinformatique.fr/linux-101.html", "lmi", "linux")
start_parse("https://www.lemondeinformatique.fr/windows-99.html", "lmi", "windows")
start_parse("https://www.lemondeinformatique.fr/macos-x-100.html", "lmi", "mac")
start_parse("https://www.lemondeinformatique.fr/os-mobile-27.html", "lmi", "os_mobile")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-produit-sur-android-75.html", "lmi", "android")
start_parse("https://www.lemondeinformatique.fr/toute-l-actualite-produit-sur-ios-21.html", "lmi", "ios")


# ---------------------- Parsage silicon.fr ----------------------

start_parse("https://www.silicon.fr/actualites/cloud/virtualization", "silicon", "virtualisation")

start_parse("https://www.silicon.fr/actualites/cybersecurite", "silicon", "cybersecurite")
start_parse("https://www.silicon.fr/actualites/security/security-management", "silicon", "politique_securite")
start_parse("https://www.silicon.fr/actualites/security/virus", "silicon", "malware")
start_parse("https://www.silicon.fr/actualites/security/cyberwar", "silicon", "cyberguerre")

start_parse("https://www.silicon.fr/actualites/cloud/datacenter", "silicon", "datacenter")
start_parse("https://www.silicon.fr/actualites/cloud", "silicon", "cloud")
start_parse("https://www.silicon.fr/actualites/cloud/server", "silicon", "cloud_serveur")

start_parse("https://www.silicon.fr/actualites/workspace/operating-system", "silicon", "os")

# ---------------------- Parsage vladan.fr ----------------------

start_parse("https://www.vladan.fr/", "vladan", "vmware")


# ---------------------- Parsage usine-digitale.fr ----------------------

start_parse("https://www.usine-digitale.fr/cybersecurite/", "ud", "cybersecurite")

