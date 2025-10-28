# cubby

[cubby](https://cubby.website) is a little directory of websites where
every website gets a point on a map.

## Features
- look at the map! (I designed it with rice!)
- click on map points - or navigator items - to discover new websites!
- find spots with silly addresses!
- read silly directions and descriptions of websites!

## About

This project was initially made for [Hack Club](https://hackclub.com/)'s [Siege](https://siege.hackclub.com/), a weekly project challenge. It was week four for me at the start of this project.

## Tech used (some of it)

### Website side
- [Svelte](https://svelte.dev/), my beloved!
- [TypeScript](https://www.typescriptlang.org/), bearable JS!
- [Vite](https://vite.dev/) - this does so many things I couldn't live without it
- [NodeJS](https://nodejs.org/) (thank you Node we all say in unison)
- [Leaflet](https://leafletjs.com/), absolutely awesome maps!
- [ky](https://github.com/sindresorhus/ky), for requests!
- [canvas-confetti](https://www.kirilv.com/canvas-confetti/) - it's confetti! Yay!

### Backend side
- [Python](https://python.org/) (yay)
- [Poetry](https://python-poetry.org/), awesome dependency manager for Python!
- [FastAPI](https://fastapi.tiangolo.com/) FASTAPI I LOVE YOU
- [dataset](https://github.com/pudo/dataset), simple database interfacing!
- [SQlite](https://sqlite.org/), database!

### Design 
- [Figma](https://figma.com/) ([check out the file I'm working on!](https://www.figma.com/design/oYrbOoAW8EHYGDetOr15jN/Untitled?node-id=0-1&t=SW7ercSQlupiDhyM-1))


## Running

This project has two parts: a backend API and the website frontend.

You should start by cloning the repo:

```bash
$ git clone https://github.com/hs7t/cubby.git
```

Specific instructions for running each part follow.

### Website

Spinning up the website is easy! From [`website`](./website/):

1. Install packages
    ```bash
    $ npm install
    ```
2. Run a development server
    ```bash
    $ npm run dev
    ```
3. Get a build when you're ready
    ```bash
    $ npm run build     # check out ./dist afterward!
    ```

### Backend

This is also easy! Making sure you've got [Poetry](https://python-poetry.org/) and
Python both installed, from [`backstage`](./backstage/):

1. Install dependencies
    ```bash
    $ poetry install
    ```
2. Run a development server
    ```bash
    $ poetry run fastapi dev 
    ```

[Deployment](https://fastapi.tiangolo.com/deployment/) is slightly trickier.


## Credits 
- [Using Leaflet with SvelteKit](https://khromov.se/using-leaflet-with-sveltekit/) by Stanislav Khromov
- [How to make a fantasy rice map](https://thecozyartteacher.com/how-to-make-a-rice-fantasy-map/) by The Cozy Art Teacher
- u/PizzaTucker's [neat trick to use an emoji as a favicon](https://www.reddit.com/r/webdev/comments/w8gx24/here_is_a_neat_trick_i_found_to_use_an_emoji_as_a/)