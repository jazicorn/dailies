Project Checklist
---

[Tutorial](https://dev.to/mdrhmn/deploying-react-django-app-using-heroku-2gfa) Used For Reference

- [ ] Customize README
- [ ] [Wireframe](https://lucid.app/lucidchart/f07614d6-25e2-4c01-95c0-78e22b780e3c/edit?beaconFlowId=23970D058C56ADC1&page=0_0#)  
  - [ ] Homepage/About 
  - [ ] Sign-up/Login
  - [ ] CRUD To-Do-List
  - [ ] CRUD Sample
  - [ ] CRUD Multiple To-Do-List
  - [ ] User Automated Task
- [X] Choose [Color Story](https://coolors.co/0fff95-414141-e3a0c3-b8b8b8-cc953e)
  - #0FFF95 Medium Spring Green
  - #414141 Onyx
  - #E3A0C3 Kobi
  - #B8B8B8 Gray X 11 Gray
  - #CC953E Harvest Gold
- [ ] Setup Backend
    - [X] pip
      - [X] Check if installed
        - pip --version
      - [X] Update if Needed
        - pip install --upgrade pip(Making sure pip is updated)
    - [X] python
      - [X] Check if python installed
        - python --version
    - [X] Create Virtual Enviroment | [venv](https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html)
      - *Tip* use virtualenvwrapper and add PATH to .bashrc
      - virtualenv venv
      - (To activate virtual enviroment)
        - source venv/bin/activate
      - (Upgrade pip in virtual enviroment)
        - pip install --upgrade pip
    - [X] Install [Django](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
        - python -m pip install Django
    - [X] Install Django Root Directory
        - django-admin startproject backend .
    - [X] Freeze Project Dependencies
        - pip freeze > requirements.txt  
- [ ] Models
  - [ ] **User**
    - [ ] *ID*
    - [ ] *Date*
      - Created At
      - Updated At
    - [ ] *Roles* // Permissions
      - Customer
    - [ ] *Settings*
      - [ ] Username
        - [ ] Public //
        - [ ] Change 
      - [ ] Email
        - [ ] Change 
      - [ ] Password
        - [ ] Change Password
      - [ ] User Statistics
    - [ ] *Profile*
      - [ ] Username
      - [ ] About
      - [ ] List(s)
    - [ ] *Dashboard*
      - [ ] *List(s)*
  - [ ] **List**
    - [ ] *ID*
    - [ ] *Date*
      - Created At
      - Updated At
      - Deleted  (Add Later, not first interation)
    - [ ] *Roles* = Bool // Public=Share/Display; Private=Don't
      - [ ] Public | Private
    - [ ] *Title* = String // Title of List
    - [ ] *Complete* = Bool// List Complete or Incomplete
    - [ ] *Tags* 
    - [ ] **Item**
      - [ ] *ID*
      - [ ] *Date*
      - [ ] *Title* // Item in list
      - [ ] *Complete* // Item Complete or Incomplete
      - [ ] *Tags* 
- [ ] Pages
  - [ ] Homepage
    - [ ] Welcome Banner
    - [ ] About
  - [ ] List
    - [ ] CRUD
  - [ ] Signup/Login
    - [ ] Username
    - [ ] E-mail
    - [ ] Password
    - [ ] Re-type Password
  - [ ] User
    - [ ] Settings
    - [ ] Profile
    - [ ] Dashboard
- [ ] Initiate Frontend | [React](https://reactjs.org/docs/create-a-new-react-app.html)
- [ ] User Automated Task | Python scripts?
- [ ] Notifications | [Twilio](https://www.twilio.com/docs)
- [ ] Deploy | [Heroku](https://devcenter.heroku.com/articles/deploying-python)


Notes
---

How do I use tags?
How do I implement tags? [Tag Schema Design](https://charlesleifer.com/blog/a-tour-of-tagging-schemas-many-to-many-bitmaps-and-more/)
Tags vs Catergories? Or both?

