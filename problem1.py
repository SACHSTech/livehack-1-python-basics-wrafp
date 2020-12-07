"""
Name: problem1.py

Purpose: To create a program that converts Celsius to Fahrenheit for the cousin to understand the climate in Canada.

Author: Huang.K

Date created: 7/12/2020
"""

print("   ---[(°C) to (°F) Converter]---")

# Input the temperature in Celsius
degrees_in_celsius = float(input("\nEnter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
degrees_in_fahrenheit = ((degrees_in_celsius * 9) / 5 + 32)

# Output the temperature in Fahrenheit
print("\nThe temperature is", degrees_in_fahrenheit, "°F")