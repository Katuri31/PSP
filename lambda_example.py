# C=[39.2,36.5,37.3,38,37.8] is a list containing temperature values in degree celsius
#using lambda function convert the above lit into a list of temperature in Farenheit.

c=[39.2,36.5,37.3,38,37.8]
f=map(lambda x:((x*9/5)+32),c)
print(list(f))
