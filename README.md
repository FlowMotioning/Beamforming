# Beamforming WUPS Project
General idea: A-mode ultrasound data from many neighboring transducers. Reconstructing these signals into images is called B-mode ultrasound. We know the depth from where the reflections originate, and should be able to attribute each change in propagation speed (of send out soundwave) at tissue borders to one transducer. The process to get the 2D brightness map from raw ultrasound data is called **beamforming**. 

- [Project Proposal Slide](<media/wups project proposal.png>)

Please refer to the [notes](notes/mindmap.md) for theory and explanation of this technology

Beamforming with DAS (Delay-and-Sum):
- [Delay and Sum](juypter/images/ex6_beamforming_das.drawio.png) concept image. The delays to each transducer from the source can create a focused and directed beam of ultrasound. Transducers are sending pulses and listening for reflections, thus serving as actuator and sensor at the same time. During B-mode imaging, the signals arriving at transducers from the same reflected object (but with slightly different delays) are "shifted" to overlap and summed together to get high amplitude signal.
    - [Delay and Sum Concept Note](notes/beamforming_DAS.md)

- [Image reconstruction](media/image_reconstruction.png)

- [Polybox Link](https://polybox.ethz.ch/index.php/apps/files/?dir=/WUPS%20Project&fileid=3513953695)

## Coding "Guidlines"

- To better enable source control the **beamformer algorithms** should NOT be in jupyter notebooks (because it is like a website and html is absolutely miserable to read in raw format)
- Code that produces output (images, arrays, other data) should be done in jupyter notebooks (because notebooks have very easy output handling) -> e.g.: call function `beamformer.py` from notebook to execute code, but produce output in jupyter. 

## PICMUS Datasets

It is basically a bad idea to put the 0.5 GB into the repo on GitHub. Therefore here are the instructions where to put the dataset downloaded from PICMUS challenge [dataset](https://www.creatis.insa-lyon.fr/Challenge/IEEE_IUS_2016/download). 
- download the .zip archive and extract into root of this project. File path should be something like this: `Beamforming/archive_to_download/read_me.txt` (only one archive_to_download folder until reaching the read_me.txt file)

For the **in vivo** [dataset](https://www.creatis.insa-lyon.fr/Challenge/IEEE_IUS_2016/download):
- `Beamforming/in_vivo/read_me.txt`

## Git and GitHub

I found [this](https://medium.com/@jonathanmines/the-ultimate-github-collaboration-guide-df816e98fb67#:~:text=How%20to%20Collaborate%20on%20GitHub%201%20%20Step,Repeat.%20And%20that%E2%80%99s%20pretty%20much%20it%21%20See%20More.) short but nice rundown of how to collaborate using Git. 

## Python Environment
- In VS Code `%matplotlib notebook` doesn't work, because it is a javascript injection into the browser (VS Code jupyter notebook is different). To still use an interactive matplotlib widget you have to install a [library](https://matplotlib.org/ipympl/) with `conda install -c conda-forge ipympl` and use `%matplotlib ipympl`. Then upon execution allow the additional downloads and choose from *Change Presentation* menu (three dots next to the output below the executed cell) to "application/vscode...widget".

# Roadmap

The BIG steps until project completion:

- [ ] Understand beamforming
- [x] Setup Project Roadmap
    - [x] Migrate ToDos to Trello
- [ ] Reconstructing Images from PICMUS dataset
    - [x] naive method (straigth beam into tissue with reflections)
    - [ ] summation from different angles to cancel out noise
- [ ] Presentation
    - [ ] decide what data we want to have presentable in the end

## Trello

I am currently working on migrating these [ToDos to trello](https://trello.com/b/LNgm3pRo), because Kanban is the better tool for project planning imo
- small [introduction to kanban](https://www.atlassian.com/agile/kanban):
    - visual representation of project (transparency and overview of work being done)
    - flexible assignment of tasks
    - flowing work because of granularity (not "sprints" where big tasks are done 1 by 1)
- detailed explanation of each step in [kanban project management](https://thedigitalprojectmanager.com/projects/pm-methodology/how-to-use-kanban-project-management/)
    - Column: This is your status view
    - Cards: holds the task or work item to be completed. Ensure you keep these tasks small and achievable
    - Feedback Loop: everyone should be part of the decision making process, through meetings establish retrospection and improvements
        -  Allows all team members to take a leadership role or accountability role
    - **kanban is as easy as moving cards between status columns!**