# Writing to an excel
# sheet using Python
import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 1, 'First Name')
sheet1.write(0, 2, 'Last Name')
sheet1.write(0, 3, 'Buisness Job Title')
sheet1.write(0, 4, 'Firm Name')
sheet1.write(0, 5, 'Multiple locations?')
sheet1.write(0, 6, 'Bank or Credit Union Relationship?')
sheet1.write(0, 7, 'Website')
sheet1.write(0, 8, 'Phone')
sheet1.write(0, 9, 'Email')
sheet1.write(0, 10, '# Employees on Website')
sheet1.write(0, 11, '# Investment Professionals')
sheet1.write(0, 12, 'FINRA?')
sheet1.write(0, 13, 'Broker Dealer (FINRA)')
sheet1.write(0, 14, 'Address')
sheet1.write(0, 15, 'Address')
sheet1.write(0, 16, 'City')
sheet1.write(0, 17, 'State')
sheet1.write(0, 18, 'Country')
sheet1.write(0, 19, 'City')
sheet1.write(0, 20, 'Postal Code')



wb.save('xlwt example.xls')
