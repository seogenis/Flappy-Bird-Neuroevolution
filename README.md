# Flappy Bird Evolution Algorithm NEAT

This project implements an evolutionary algorithm using NEAT (NeuroEvolution of Augmenting Topologies) to train a set of birds to play the game Flappy Bird. The project is built using Python and Pygame.

## Project Overview

The goal is to evolve a population of birds over generations to improve their ability to navigate obstacles in the game. The birds' neural networks are initialized with random weights and biases, and through the process of evolution, the fittest birds are selected to create offspring with slight variations in their neural networks.

### Key Features
- **Random Initialization**: Weights and biases are initialized between -1 and 0 using a sigmoid activation function.
- **Neural Network Architecture**: 
  - Hidden Layer 1: 3 neurons
  - Hidden Layer 2: 1 neuron
  - Sigmoid activation function for all neurons
- **Evolution Process**: 
  - Top-performing birds are selected as parents.
  - Offspring are generated with slight mutations in weights and biases.
  - Fitness is determined by the time a bird survives in the game.

## Classes and Methods

### `randomise_WB`
Initializes a population of birds with random weights and biases.

### `active_birds`
Manages the population of birds, including:
- **new_gen**: Generates a new generation of birds based on the fittest birds from the previous generation.
- **bird_decision**: Determines the bird's decision (flap or not) based on its neural network output.
- **run_game**: Runs the game for a given bird, handling the game loop, obstacle generation, collision detection, and scoring.

### `bird_data` (Planned Feature)
A class to store and analyze data from multiple generations, including:
- Average fitness
- Fitness distribution
- Plotting capabilities

## Usage

To run the simulation, use the following structure:
1. Initialize the population with `randomise_WB()`.
2. Create an `active_birds` object with the list of initialized birds.
3. Run the game for each bird and evolve over a set number of generations.

```python
a_list = randomise_WB()
a = active_birds(a_list)

generations = 20
for i in range(generations):
  for bird in a.birds_list:
    a.run_game(bird)
  
  a.new_gen()
