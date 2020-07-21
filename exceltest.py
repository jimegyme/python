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

rowcount = 1
num_employees = len(self.employees['FirstName'])
i = 0
while i < num_employees:
      sheet1.write(rowcount,1, self.employees['FirstName'][i])
      sheet1.write(rowcount,2, self.employees['LastName'][i])
      sheet1.write(rowcount,3, self.employees['JobTitle'][i])
      sheet1.write(rowcount,8, self.employees['Phone'][i])
      sheet1.write(rowcount,9, self.employees['Email'][i])


      sheet1.write(rowcount,4, self.firm_name)
      sheet1.write(rowcount,5, self.multiple_locations)
      sheet1.write(rowcount,6, self.bank_or_credit_union)
      sheet1.write(rowcount,7, self.website)
      sheet1.write(rowcount,10, num_employees)
      sheet1.write(rowcount,11, self.num_investment_professionals)
      sheet1.write(rowcount,12, self.finra)
      sheet1.write(rowcount,13, num_employees)
      sheet1.write(rowcount,14, self.address_street)
      sheet1.write(rowcount,15, self.address_apt)
      sheet1.write(rowcount,16, self.address_city)
      sheet1.write(rowcount,17, self.address_state)
      sheet1.write(rowcount,18, self.Country)
      sheet1.write(rowcount,19, self.address_city)
      sheet1.write(rowcount,20, self.address_postal_cose)



      rowcount ++
      i++


wb.save('xlwt example.xls')
