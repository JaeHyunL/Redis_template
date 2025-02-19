print ("Hello, World!")

-- local value, global value 변수 존재
local value = 10 + 1

print(value)

-- LuA if statement 
if value > 0 then
  print("value is postive")
end

-- not equal is tilde(틸데, 물결표)
if value ~= 0 then
  print("value is non zero")
end

if value == 11 then
  print("value is 11")
end

-- start from index 1
local country = {"South Korea", "United States", "Japan"}

-- get value of index
print(country[1])
-- length function
print(#country)

-- table insert
table.insert(country, 'China')
print(country[4])


-- Like python enumerate
for i, v in ipairs(country) do
  print(i, v)
end 

-- Set Key Value data structure
local car = {color = "White", name = "tesla"}
print(car['name'])

-- Like Python items
for k, v in pairs(car) do
  print(k, v)
end
