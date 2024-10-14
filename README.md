# cloudExamples

Some examples of ml code using cloud computing.

## Supporting material

Here you can find a bash cheatsheet:

[Bash Commands]: https://icosbigdatacamp.github.io/2018-summer-camp/slides/BASH_Cheat_Sheet.pdf

## Initial Set-Up

Install Docker and Git
```
sudo apt-get update
sudo apt-get install git docker-compose
```
Clone the repo in Git
```
git clone https://github.com/hdg7/cloudExamples.git
```

## Deploy the specific system
In the specific folder:
```
sudo docker build . -t example
sudo docker run -it -p XXXX:YYYY -v local_folder:vm_folder example
```
where XXXX is the local port to redirect to YYYY in the container, local_folder the folder to share and vm_folder the folder inside of the container.
