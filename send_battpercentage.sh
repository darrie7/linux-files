#!/bin/sh

my_var=$(cat /sys/class/power_supply/BAT1/capacity)
data='{"battery": '$my_var'}'
#curl -i -X "POST" -d "$data" -H "Content-Type: application/json" -H "Accept: application/json" https://jsonblob.com/api/jsonBlob

curl -i -X "PUT" -d "$data" -H "Content-Type: application/json" -H "Accept: application/json" https://jsonblob.com/api/jsonBlob/1145508021702352896
