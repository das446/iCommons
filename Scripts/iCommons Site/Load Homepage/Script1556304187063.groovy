import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable

'User opens a web browser and navigates to http://rack113.cs.drexel.edu/\r\n\r\nUser is presented with a functional homepage for the iCommons App\r\nCCI logo caption is present on the page.\r\nA list of occupied rooms are displayed on the page.\r\nA list of available rooms are displayed on the page.\r\nUser is allowed to scroll when viewing the list of occupied rooms.\r\nMiddle section of the page consists of a CCI photo and caption that the Administrator changes.\r\nSite footer is displayed at the bottom of the screen.\r\nAdvanced Search button is located at the bottom of the screen.\r\nUser is able to view background image.\r\n'
WebUI.openBrowser('http://rack113.cs.drexel.edu/')

'User waits for page to load'
WebUI.waitForPageLoad(6)

WebUI.delay(3)

