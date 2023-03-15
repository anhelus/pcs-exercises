<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/anhelus/pcs-exercises">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Python for Data Science - Exercises</h3>

  <p align="left">
    This repository holds the exercises for the "Python for Data Science" course, in Italian.
    <br />
    <a href="https://github.com/anhelus/pcs-exercises"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/anhelus/pcs-exercises/issues">Report Bug</a>
    ·
    <a href="https://github.com/anhelus/pcs-exercises/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>

  1. [About The Project](#about-the-project)
  2. [Built With](#built-with)
  3. [Getting Started](#getting-started)
      * [Prerequisites](#prerequisites)
      * [Installation](#installation)
  4. [Usage](#usage)
  5. [Roadmap](#roadmap)
  6. [Contributing](#contributing)
  7. [License](#license)
  8. [Contact](#contact)
  9. [References](#references)

</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Jupyter](https://jupyter.org/)
* [Colab](https://colab.research.google.com/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Be sure to have these software installed:

* [Python](https://www.python.org/downloads/) in a recent release (3.8+)
* [Pipenv](https://pipenv.pypa.io/):
  ```sh
  pip install pipenv
  ```
* or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/):
  ```sh
  pip install virtualenvwrapper
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/anhelus/pcs-exercises.git
   ```
2. Install required packages
    
    **Option 1** - Using `pipenv`

      ```sh
      pipenv install
      ```
    
    **Option 2** - Using `pip` and `virtualenvwrapper`:

      ```sh
      $ mkvirtualenv pcs
      $ workon pcs
      (pcs) $ pip install -r requirements.txt
      ```

> Note: with `pip`, a virtual environment is *strongly* suggested.

<!-- USAGE EXAMPLES -->
## Usage

This repository can be used directly with Jupyter. Activate your virtual environment, then run:

```sh
jupyter-notebook
```

This will launch the Jupyter server locally. Otherwise, you can use a Colab instance.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/anhelus/pcs-exercises/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

<!-- CONTACT -->
## Contact

[Angelo Cardellicchio](mailto:angelo.cardellicchio@stiima.cnr.it)

Project Link: [https://github.com/anhelus/pcs-exercises](https://github.com/anhelus/pcs-exercises)

## References

* [NumPy docs](https://numpy.org/doc/)
* [Matplotlib docs](https://matplotlib.org/stable/index.html)
* [Seaborn docs](https://seaborn.pydata.org/tutorial.html)
* [Pandas docs](https://pandas.pydata.org/docs/)
* [Scikit Learn docs](https://scikit-learn.org/stable/user_guide.html)
* [TensorFlow docs](https://www.tensorflow.org/learn?hl=en)
* [YOLOv8 docs](https://docs.ultralytics.com/)
* [tf-explain docs](https://tf-explain.readthedocs.io/en/latest/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anhelus/pcs-exercises.svg?style=for-the-badge
[contributors-url]: https://github.com/anhelus/pcs-exercises/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anhelus/pcs-exercises.svg?style=for-the-badge
[forks-url]: https://github.com/anhelus/pcs-exercises/network/members
[stars-shield]: https://img.shields.io/github/stars/anhelus/pcs-exercises.svg?style=for-the-badge
[stars-url]: https://github.com/anhelus/pcs-exercises/stargazers
[issues-shield]: https://img.shields.io/github/issues/anhelus/pcs-exercises.svg?style=for-the-badge
[issues-url]: https://github.com/anhelus/pcs-exercises/issues
[license-shield]: https://img.shields.io/github/license/anhelus/pcs-exercises.svg?style=for-the-badge
[license-url]: https://github.com/anhelus/pcs-exercises/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/angelocardellicchio
