import os

import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_AssgnFileupload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    files = ["uploads\Test1.txt", "uploads\ClassNotes.txt"]

    #filesToUpload
    page.locator("#filesToUpload").set_input_files(files)

    page.wait_for_timeout(5000)

    Files= page.locator("#fileList li").all()

    print("The following files were uploaded:")

    for file in Files:
        filename = file.inner_text()
        print(filename)

    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("Test1.txt")
    expect(page.locator("#fileList li:nth-child(2)")).to_have_text("ClassNotes.txt")

def test_AssgnFileDownload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.locator("#inputText").fill("welcome")

    page.locator("#generatePdf").click()

    page.on("download", lambda download: download.save_as("downloads/testfile.pdf"))

    page.locator("#pdfDownloadLink").click()

    page.wait_for_timeout(3000)

    if os.path.exists("downloads/testfile.pdf"):
        print("File exists")
    else:
        print("File not exist")







