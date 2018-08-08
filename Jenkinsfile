pipeline {
  	agent any
  
	stages{
		stage('Package polls app into a pip package'){
			steps{
				sh 'cd polls'
				sh 'python setup.py sdist'
			}
		}
	}

	stages{
		stage('Install polls package'){
			steps{

				sh 'pip install --user polls/dist/polls-0.1.tar.gz'
			}
		}
	}
	
	stages{
		stage('Commit the packaged web-app'){
			steps{
				sh 'git add .'
				sh 'git commit -m "polls package updated"'
				sh 'git push origin master'
			}
		}
	}

	stages {
	    stage('Start Postgres server') {
		    steps {
		       
	            	sh 'docker exec -i reverent_jackson service postgresql restart'
	                 
		    }
		}
	}

    stage('Run django server'){
    	steps{
    		sh 'python manage.py runserver'
    	}
    }
  
}