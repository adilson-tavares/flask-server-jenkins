pipeline {

  // environment {
  //   IMAGENAME = "service-flask"
  //   IMAGE = "${NAME}:${VERSION}"
  //   // dockerImage = ""
  // }
  environment {
    registryCredential = credentials('docker-hub-credential')
    IMAGENAME = "service-flask"
    IMAGE = "${NAME}:${VERSION}"
    VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
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

  stages {
    stage('Checkout Source') {
      steps {
        git branch: 'main', url: 'https://github.com/adilson-tavares/flask-server-jenkins.git'
        // credentialsId: 'github-credentials'
      }
    }
    stage('Build image') {
      steps{
        // script {
        //   dockerImage = docker.build dockerimagename
        // }
        container('docker') {
          //  sh 'docker build -t tavarescruz/python-flask:latest .'
            echo "for branch ${env.BRANCH_NAME}"
            sh "docker build -t tavarescruz/${IMAGENAME} ."
            sh "docker tag ${IMAGENAME}:latest tavarescruz/${IMAGENAME}:${VERSION}"
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
          sh "docker push tavarescruz/${IMAGENAME}:${VERSION}"
        }
      }
    }

    // stage('Checkout Source k8s manifest') {
    //   steps {
    //     git branch: 'main', url: 'https://github.com/adilson-tavares/jenkins-webhook.git',
    //     // credentialsId: 'github-credential'
    //   }
    // }

    stage('Update K8S manifest & push to Repo'){
      steps {
        git branch: 'main', url: 'https://github.com/adilson-tavares/jenkins-webhook.git'
          script{
            // withCredentials([gitUsernamePassword(credentialsId: 'github-credential',
            //      gitToolName: 'Default')]) {


                // git branch: 'main', url: 'https://github.com/adilson-tavares/jenkins-webhook.git',
                // credentialsId: 'github-credential'
              // withCredentials([gitUsernamePassword(credentialsId: 'github-credential', gitToolName: 'git-tool')]) {
                  sh " cat flask-service/deploy.yaml"
                  sh " sed -i 's/service-flask.*/${IMAGENAME}:${VERSION}/g' flask-service/deploy.yaml"
                  sh " cat flask-service/deploy.yaml "
                  sh " git add flask-service/deploy.yaml "
                  sh " git commit -m 'Updated the deploy yaml | Jenkins Pipeline' "
                  // sh " git remote -v "
                  sh " git push -u origin main "
                                         
              }
          // }
      }
        }


    // stage('Deploying flask python container to Kubernetes') {
    //    // steps('Apply Kubernetes files') 
    //    steps{
    //           //  withKubeConfig([credentialsId: 'jenkins-kind', serverUrl: 'https://192.168.49.2:8443']) {
    //             sh 'kubectl apply -f deploy.yaml'
    //             sh 'kubectl apply -f service.yaml'
    //         //  }
    //     }

    // }

  }

    // node (POD_LABEL){

    // }
  post {
    always {
      container('docker') {
        sh 'docker logout'
      }
    }
  }

}