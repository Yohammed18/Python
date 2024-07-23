# Declare an empty list
empty_list = []
# Declare a list with more than 5 items
list_of_five = [1,2,3,4,5]
# Find the length of your list
print(len(list_of_five))
# Get the first item, the middle item and the last item of the list
print(f"First item: {list_of_five[0]}\nMiddle Item: {list_of_five[2]}\nLast Item: {list_of_five[-1]}")
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['James Brown', 34, 5.11, "single", '620 John Paul Jones']
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Print the list using print()
print(it_companies)
# Print the number of companies in the list
print(f"Companies count: {len(it_companies)}")
# Print the first, middle and last company
print(f"First company: {it_companies[0]}\nMiddle company: {it_companies[3]}\nLast company: {it_companies[-1]}")
# Print the list after modifying one of the companies
it_companies[4] = "NVDIA"
print(it_companies)
# Add an IT company to it_companies
it_companies.append("Intel")
# Insert an IT company in the middle of the companies list
it_companies.insert(4, "AMD")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
join_company = '#;  '.join(it_companies)
print(join_company)
# Check if a certain company exists in the it_companies list.
print(it_companies.index("Google"))
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
print(sorted(it_companies, reverse=True))
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies[:-3])
# Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)
# Remove the first IT company from the list
del it_companies[0]
print(it_companies)
# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(f"{full_stack}")
# Exercises: Level 2 - The following is a list of 10 students ages:
import math
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
print(f"min= {ages[0]}, max={ages[-1]}")
# Add the min age and the max age again to the list
ages.append(ages[-1])
ages.append(ages[0])
print(ages)
# Find the average age (sum of all items divided by their number )
count = sum(ages)
avg_age = int(count/len(ages))
print(f"Average age: {avg_age}")
# Find the range of the ages (max minus min)
max_age = max(ages)
min_age = min(ages)
age_range = max_age - min_age
print(age_range)
# Find the middle country(ies) in the countries list
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

middle = len(countries)//2
print(f"Middle Country: {countries[middle]}")
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
chi, rus, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(scandic)
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:middle]
second_half = countries[middle:]

