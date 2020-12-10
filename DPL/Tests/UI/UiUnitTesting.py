import main
import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt


class UITests():
    def test_defaults(self):
       '''Test the GUI in its default state'''
       self.assertEqual(self.form.ui.one.value(), 1)
       self.assertEqual(self.form.ui.two.value(), 2)
       self.assertEqual(self.form.ui.three.value(), 3)
       self.assertEqual(self.form.ui.four.value(), 4)
       self.assertEqual(self.form.ui.five.value(), 5)
       self.assertEqual(self.form.ui.six.value(), 6)
       self.assertEqual(self.form.ui.seven.value(), 7)
       self.assertEqual(self.form.ui.eight.value(), 8)
       self.assertEqual(self.form.ui.nine.value(), 9)
       self.assertEqual(self.form.ui.zero.value(), 0)

       SubmitWidget = self.form.ui.buttonBox.button(self.form.ui.submit.Ok)
       backspaceWidget = self.form.ui.buttonBox.button(self.form.ui.backSpace.Ok)
       CancelWidget = self.form.ui.buttonBox.button(self.form.ui.Cancel.Ok)
       QTest.mouseClick(SubmitWidget, Qt.LeftButton)
       QTest.mouseClick(backspaceWidget, Qt.LeftButton)
       QTest.mouseClick(CancelWidget, Qt.LeftButton)
    def test_Buttons(self):
        '''Test the blender speed buttons'''
        self.form.ui.speedButton1.click()
        self.assertEqual(self.form.speedName, "&Mix")
        self.form.ui.speedButton2.click()
        self.assertEqual(self.form.speedName, "&Whip")
        self.form.ui.speedButton3.click()
        self.assertEqual(self.form.speedName, "&Puree")
        self.form.ui.speedButton4.click()
        self.assertEqual(self.form.speedName, "&Chop")
        self.form.ui.speedButton5.click()
        self.assertEqual(self.form.speedName, "&Karate Chop")
        self.form.ui.speedButton6.click()
        self.assertEqual(self.form.speedName, "&Beat")
        self.form.ui.speedButton7.click()
        self.assertEqual(self.form.speedName, "&Smash")
        self.form.ui.speedButton8.click()
        self.assertEqual(self.form.speedName, "&Liquefy")
        self.form.ui.speedButton9.click()
        self.assertEqual(self.form.speedName, "&Vaporize")
    def test_numberPad(self):
        '''Test
        testing different combinations
        '''
        self.setFormToZero()
        self.form.ui.iceHorizontalSlider.setValue(4)

        # Push OK with the left mouse button
        okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
        QTest.mouseClick(okWidget, Qt.LeftButton)
        self.assertEqual(self.form.jiggers, 4)
