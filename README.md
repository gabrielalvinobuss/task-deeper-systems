# Instructions

This repository contains two folders, one for the backend using Python and MongoDB, and another for the frontend using VueJS and PrimeVue.

To run the project, both the backend and frontend need to be running simultaneously.

First, to insert the contents of the udata.json file into MongoDB, you need to run parser.py

To start the backend, you need to run the following command inside the backend folder:

```sh
flask run
```

The first time you run the frontend, you need to install the dependencies.

## Project Setup

```sh
npm install
```

After installing the dependencies, you can start the frontend from within the frontend folder.

### Compile and Hot-Reload for Development

```sh
npm run dev
```

## Things I would do differently if I had more time:

Update by ID instead of by username, check why the CSS classes are not working and fix them, add more documentation, improve the design.