while True:
    start_year=int(input("\nGive the start year for range of array: "))
    end_year=int(input("\nGive the end year for range of array: "))
    leap_year=[]
    if start_year < end_year:
        for i in range(start_year,end_year):
            if i%4==0 and i%400!=0:
                leap_year.append(i)
        if not leap_year:
            print("\nThere is no leap year in given range.")
        else:
            print(f"\nThe leap years in given range are : {leap_year}")
        break
    else:
        print("\nPlease give start year less than end year.")
'''
Output:
Case 1)

Give the start year for range of array: 2030

Give the end year for range of array: 2024

Please give start year less than end year.

Give the start year for range of array: 2000

Give the end year for range of array: 2024

The leap years in given range are : [2004, 2008, 2012, 2016, 2020]

Case 2)

Give the start year for range of array: 2000   

Give the end year for range of array: 2003

There is no leap year in given range.
'''