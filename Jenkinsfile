pipeline {

  // environment {
  //   dockerimagename = "tavarescruz/react-app"
  //   dockerImage = ""
  // }
  environment {
    registryCredential = credentials('docker-hub-credential')
  }

  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: docker
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
             - mountPath: /var/run/docker.sock
               name: docker-sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock    
        '''
    }

  }

    // agent {
    //     docker { image 'node:18.16.0-alpine' }
    // }

  // environment {
  //   DOCKERHUB_CREDENTIALS = credentials('dokcerhub-credentials')
  // }

  stages {
    stage('Checkout Source') {
      steps {
        git branch: 'main', url: 'https://github.com/adilson-tavares/flask-server-jenkins.git',
        credentialsId: 'github-credentials'
      }
    }
    stage('Build image') {
      steps{
        // script {
        //   dockerImage = docker.build dockerimagename
        // }
        container('docker') {
           sh 'docker build -t tavarescruz/python-flask:latest .'
        }
      }
    }
    stage('Pushing Image') {

      steps {
        container('docker') {
          sh 'echo $registryCredential_PSW | docker login -u $registryCredential_USR --password-stdin'
        }
      }
      // environment {
      //          registryCredential = 'docker-hub-credential'
      //      }
      // steps{
      //   script {
      //     docker.withRegistry( 'https://registry.hub.docker.com', registryCredential ) {
      //       dockerImage.push("latest")
      //     }
      //   }
      // }
    }
    stage('Push Image to DockerHub') {
      steps {
        container('docker') {
          sh 'docker push tavarescruz/python-flask:latest'
        }
      }
    }


    // stage('Deploying flask python container to Kubernetes') {
    //   steps {
    //     // container('docker') {
    //     //   kubernetesDeploy(configs: "deploy.yaml", "service.yaml", kubeconfigId: "jenkins-kind")
    //     // }
    //     container('docker') {
    //         sh "kubectl apply -f deploy.yaml"
    //         sh "kubectl apply -f service.yaml"
    //     }
    //   }
    // }

    stage('Apply Kubernetes files') {
      withKubeConfig([credentialsId: 'jenkins-kind', serverUrl: 'https://192.168.49.2:8443']) {
        sh 'kubectl apply -f deploy.yaml'
    }
    }

  }

    // node (POD_LABEL){

    // }
  post {
    always {
      sh 'docker logout'
    }
  }

}