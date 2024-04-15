### assignment4

# *PetPal Haven*

#### *From Shelter to Hearts: Our promise to pet-kind.*

---

## The Team: 
* [**Adele Cousins**](https://github.com/adelikinz)
* [**Cynthia Nzeh**](https://github.com/Cynth2208) 
* [**Rebecca Clarke**](https://github.com/Rclarkeweb)
* [**Nasra Diini**](https://github.com/diinin9)

#### Here is some information about us:

<details>
<summary>About Adele</summary>
Hello, my name is Adele and im based in Bristol. im a student on the CFG Degree Spring '24 cohort for software engineering.

---

Fact about me:
* I have two gerbils named bean and toast which I adore and spoil way too much.
* I love playing video games, I have a love hate relationship with counterstrike 2 (cs2)
* I also love to read, I prefer reading biographies, but I also enjoy an occasional fantasy novel too 

<details>
<summary> My Tech journey </summary>
before joining the CFG Degree Spring course I actually never wrote code before. for years before I was always put off 
as I thought it looked complicated. Early December I was encouraged to give it a try and I started by researching 
and reading basic guides on python. this then developed a passion and made me look for ways to pursue education further.

</details>

</details>
&nbsp;  
<details>
<summary>About Cynthia</summary>
Howdy guys! I'm Cynthia and I am currently based in Buckinghamshire. I am a student of the CFG Degree Spring '24 cohort.

---

Fact about me:
* I am a movie **FANATIC**! Currently making my way through classic 90's movies. Coming-of-age indie films are my fav.
* I've recently made it my mission to learn how to ski - getting there!
* I have a really peculiar, irrational fear of closely packed holes: Trypophobia... *shiversss*.

<details>
<summary> My Tech journey </summary>

I started teaching myself the basics of Javascript in December 2023 a few months before starting the CFG degree.
I have so far created projects using SQL and Python. I aim to continue improving my learning as the course progresses.
  
</details>

</details>  
&nbsp;
<details>
<summary>About Rebecca </summary>
Hello World! I'm Rebecca and currently a student on the Code First Girls Degree, on the Software Engineering pathway.

---

Facts about me:
* I absolutely love reading! And browsing bookshops!
* I enjoy training my Cavapoo puppy who's a little crazy
* I'm also mildly obsessed with pangolins and sloths

<details>
<summary> My Tech journey </summary>

I have been teaching myself to code for a while and love getting things to work without bugs.
I'm an aspiring Software Developer.
  
</details>
</details>
&nbsp;
<details>
<summary>About Nasra</summary>
Hello CFG! I'm Nasra, and I am from Birmingham!

---

Facts about me:

* I enjoy travelling and have travelled to over 20 countries so far (more is yet to come!)
* I really enjoy hiking and it's something that I like to do with my family. 
* I **love** sushi... *nomnomnom*.

<details>
  <summary> My Tech journey </summary>

I am currently in the Software Stream with the CFG where I am learning more about SQL and python
every day. It has been an ~~challenging~~ enjoyable experience thus far, and I am excited to learn loads more 
during specialisation!

  
</details>
</details>

---

## About our project

The "I Need a Pet" project was started by our non-profit organisation in collaboration with the 'Rescue Buttons' animal shelter. 
We started the project in the hopes that we can afford customers the opportunity to experience pet ownership without the 
need for long-term commitment. Through the 'PetPal Haven', customers have a choice of a variety of different pets to 
care for their chosen time period. Should customers develop a special bond with their chosen pet and wish to provide them with a more permanent 
home, we are able to facilitate the adoption process.

### Built with
[![Languages used](https://skillicons.dev/icons?i=python,flask,mysql,git&perline=20)](https://skillicons.dev)

### Tools used
[![Tools used](https://skillicons.dev/icons?i=github,postman,pycharm&perline=20)](https://skillicons.dev)


---

## Our files

#### .gitignore
A .gitignore file tells git which files, directories or patterns in your project to ignore and not to track.  
The .gitignore file is created with a `.` at the beginning.  
Each line the .gitignore file indicates a new file, folder or pattern to ignore.  
A .gitignore file is usually located and found in the root directory of the project or repository.
  
#### requirements.txt
requirements.txt is a text file that lists all the packages, modules and libraries that the project needs to run. 
Or, in other words, it lists the projects dependencies.  
Within this file the dependencies can have a specified version listed that the project has used.
The syntax is displayed as: `flask==3.0.3`  
To install the necessary project dependencies in your virtual environment you can use:  
`pip install -r requirements.txt` 
Once the packages are installed you can import them into your files.

## Installing and using our API
---
<details>

Welcome to pet haven :dog:

Pet haven is a place where people can come and experience the joys of having a pet, without worrying about all the hassle, fuss or initial commitments!

To experience this joy, please follow the below instructions:

1. Open up Pycharm or another IDE of your choice and open up the terminal.
2. Navigate to the directory where you want to clone this repository.
3. Clone the repository by copying and pasting the below in your terminal:
	`git clone https://github.com/adelikinz/assignment4.git`
4. Install the following packages via the terminal:

pip install flask (pip3 install flask for mac user)
pip install requests (pip3 install requests for mac user)
pip install mysql-connector-python (pip3 install mysql-connector-python for mac user)
import JSON and from datetime import datetime at the top of the main.py file.

5. Open up mySQL workbench and copy and paste our pet_haven database from the pethaven_db.sql file & execute this code on the workbench to create the pet_haven database.
6. Update the config.py file with your mySQL Host, User and Password information. This is necessary for connecting the Flask application to the MySQL database.
7. If necessary, change the root of the host_url in the main.py and app.py file if another application on your machine is already using port 5000.
8. Run the app.py file first and then run the main.py file on Pycharm.
9. Follow the prompts that appear in the terminal to see what animals we have at pet haven (and you want to possible rent/adopt).
10. Once you have pressed run on the app.py file, you can also access the API via the web browser or Postman using the host_url found in main.py (host_url = 'http://127.0.0.1:5000’). For example, to access all available pets you would have to make a GET request on Postman: http://127.0.0.1:5000/pets
11. If you experience any issues, please check the terminal where Flask is running and follow the instructions of any error messages that may appear on there. 

  
</details>





## Project Screenshots
<details>
### checking status, created a new file, added the file to a branch & committing with a meaningful message: 

![image](https://github.com/adelikinz/assignment4/assets/108008511/5c8b5d11-060b-4538-bb5b-bd84b88b0d0f)  


![image](https://github.com/adelikinz/assignment4/assets/108008511/0d3c4a4c-419f-4637-8fd2-1d9d5693e1bf)  
### created a new branch
![image](https://github.com/adelikinz/assignment4/assets/108008511/315d638e-d6d1-41d7-b8e2-3b1a1de84e48) 

### opening a pull request



</details>

