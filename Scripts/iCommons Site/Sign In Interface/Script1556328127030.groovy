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

WebUI.click(findTestObject('Sign In link'))

WebUI.waitForPageLoad(5)

WebUI.delay(2)

WebUI.click(findTestObject('Username field'))

WebUI.delay(1)

WebUI.setText(findTestObject('Username field'), 'test')

WebUI.delay(1)

WebUI.click(findTestObject('Password field'))

WebUI.delay(1)

WebUI.setText(findTestObject('Password field'), 'test')

WebUI.delay(1)

WebUI.click(findTestObject('Sign In button'))

WebUI.waitForPageLoad(5)

WebUI.delay(3)

WebUI.click(findTestObject('Username field'))

WebUI.delay(1)

WebUI.setText(findTestObject('Username field'), 'jtp53')

WebUI.delay(1)

WebUI.click(findTestObject('Password field'))

WebUI.setText(findTestObject('Password field'), 'testone23')

WebUI.delay(1)

WebUI.click(findTestObject('Sign In button'))

WebUI.waitForPageLoad(5)

WebUI.delay(3)

