# SlamAI: Basketball Analytics
Senior Seminar project for a desktop application that counts makes and misses in a basketball game using artificial intelligence. Current implementation allows for use and analysis of images. Further implementation of video analysis is planned. 

## How To Use
In order to run a local instance of the project simply clone the repo and run the main.py file. This file will launch the application and create any necessary dependent folders in the directory that the project was cloned to.

Upon launching of the program, the user should navigate to the "Upload" menu using the side navbar. From here the user can then upload any footage(images) that they would like to be analyzed. Once the footage is added to the system it will then needed to be grouped into the associated game.

To accomplish this, the user will navigate to the corresponding "Games" menu using the side navbar. From here the user will then be able to create new games, add footage to games, remove footage from games, rename games, run AI analysis on the selected game, and view any past analyses.

## Roadmap
Primary change to be made is refactoring the codebase to move away from Python/PyQt. The library has been a wonderful learning experience but is nonetheless difficult to work with at times and has less documentation compared to other solutions. In this process the codebase will also be refactored to institute more best practices and design principles, making the code more reusable and easier to implement changes moving forward.

Next would be to add video analysis to the system. This would make the system much more useful/practical. This would also allow the system to generate more meaningful statistics.

The final "concern" at the moment is making the program more visually appealing. There are several aspects that have every little formatting and are solely built around function. While acceptable for now this is a change that should be implemented down the line.
