# DigitalOceanKubernetesChallenge

## Purpose

This is a proof of concept deployment of a simple Python stub and MongoDB, intended to showcase containerization of my fantasy football webapp [sleeperPy](https://github.com/wbollock/sleeperPy).

A simple Python docker container grabs player data from Sleeper Fantasy Football and imports it into a MongoDB collection. I hope to eventually pair this with a web frontend of Kubernetes use, ideally seperated out into microservices. The current stub would be nice with the Kubernetes CronJob object.

## Usage

Using a `kubectl` file from your cloud provider, run the deployment.