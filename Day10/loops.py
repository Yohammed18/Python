# Loops are a fundamental programming construct that allow you to execute a block of code repeatedly. The types of loops in +
# most programming languages are for loops, while loops, do-while.

# Iterate 0 to 10 using for loop, do the same using while loop.
print('For Loop')
for i in range(0,11):
    print(i)
print("\nWhile Loop")
i = 0
while i < 11:
    print(i)
    i+=1

print('\nBackword') 
# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1,-1):
    print(i)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('\nTriangle')
for i in range(1,8):
    print(i*'#')
    
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('\nGrid')
for i in range(8):
    for x in range(8):
        print('#', end=' ')
    print()
    
# Print the following pattern:
print('\nMultiplication')
for i in range(11):
    print(f'{i} x {i} = {i*i}')
    
    
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
python_libraries = ['Python', 'Numpy','Pandas','Django', 'Flask']
print('\n')
for library in python_libraries:
    print(library)
print('\nEven Numbers')
# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i%2 == 0:
        print(i, end=" ")
print("\nOdd Numbers")
# Use for loop to iterate from 0 to 100 and print only odd numbers 
for i in range(101):
    if i%2 == 1:
        print(i, end=" ") 
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print('\n')
even_count = 0
odd_count = 0
for i in range(101):
    if i%2 == 0:
        even_count+=i
    else:
        odd_count+=i
print(f'The sum of all evens is {even_count}. And the sum of all odds is {odd_count}.')
print()
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit)-1, -1, -1):
    print(fruit[i])
print() 
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
 
for country in countries:
    if 'land' in country:
        print(f'Country: {country}')   
    



















