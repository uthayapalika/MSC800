#!/bin/bash

while true
do
  git add .
  git commit -m "Auto update"
  git push
  sleep 10
done
