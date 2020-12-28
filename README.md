## Dump-and-Fun
Ever look at that pile of files on your desk and wonder why in the world anybody still uses physical paper? With Dump and Fun, simply drop in the papers you've picked up during the day and watch as they're automatically scanned, sorted, and stored on your computer according to subject.

The Dump and Fun project was initially developed by Asher Lipman, Kathryn Merckel, Nayanthara Sajan, and Saleh Hassen at the 2020 Big Red Hackathon at Cornell. The goal was simple, figure out how automation could be used to improve the lives of ordinary college students. As we hauled our two ton backpacks to the nearest workspace, we realized that a simple way to organize and back-up the hundreds of papers we pick up throughout the day would be worth its weight in gold. Combining our knowledge of computer-vision, CAD design, and Raspberry Pi microcomputing, we decided to create a product which could process all the spare paper we're given and convert it into an easily searchable digital directory.

Installation Instructions:

First and foremost, this is only the software portion of the Dump and Fun. A future goal is to add a list of both RaspberryPi and CAD components necessary to make the product work, but for now this project will only host the software necessary to make it run. 

Secondly, this project requires several libraries in order to intergrate RaspberryPi components effectively. These libraries are all found in the projects requirements file, and can be installed using python's universal pip installer. Navigate to the directory this project's downloaded on and run this command in your computer's command line:

pip install -r requirements.txt

