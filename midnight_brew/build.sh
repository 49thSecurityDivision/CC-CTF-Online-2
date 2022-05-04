#!/bin/bash
#buildscript goes into the folder with all the .java's

#remove old
rm -rf ./build

#build
javac -d ./build *.java

#move to build
cd ./build

#make the jar thingy
mkdir META-INF
echo "Main-Class: Main" > ./META-INF/MANIFEST.MF

#package
jar cmvf META-INF/MANIFEST.MF sim.jar .

#runnable
chmod +x ./sim.jar

echo done
