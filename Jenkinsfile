/*******************************************************************************
 * Copyright (c) 2020 - Fundação CERTI
 * All rights reserved.
 *******************************************************************************/

pipeline {
    agent none
    options {
        timeout(time: 1, unit: 'HOURS')
    }
    triggers {
        cron('H 03 * * *')
    }
    environment {
        GIT_DEV_BRANCH = "develop"
    }
    stages {
        stage('Models') {
            agent any
            stages {
                stage('Install requirements') {
                    steps {
                        sh 'python3 -m pip install -r requirements.txt'
                    }
                }
                stage('Lint') {
                    steps {
                        dir('src') {
                            sh 'python3 -m prospector'
                        }
                    }
                }
                stage('Tests') {
                    steps {
                        dir('src/tests') {
                            sh 'python3 -m pytest -ra --junitxml=unittest.xml'
                        }
                    }
                }
                stage('Coverage') {
                    steps {
                        dir('src/tests') {
                            sh 'python3 -m pytest --cov --cov-report=xml --cov-report=term'
                        }
                    }
                }
            }
        }/**
        post {
            always {
                node('server 3'){
                    dir('scripts') {
                        sh 'python3 devenv.py clean'
                    }
                }
            }
            cleanup {
                node('server 3'){
                    cleanWs()
                }
            }
        }**/
    }
}