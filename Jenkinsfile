pipeline {
  	agent any
  
	stages{
		stage('Package polls app into a pip package'){
			steps{
				sh 'python polls/setup.py sdist'
			}
		}

		stage('Install polls package'){
			steps{

				sh 'pip install --user polls/dist/polls-0.1.tar.gz'
			}
		}

	    stage('Start Postgres server') {
		    steps {
		       
	            	sh 'docker exec -i reverent_jackson service postgresql restart'
	                 
		    }
		}
	

	    stage('Run django server'){
	    	steps{
	    		sh 'python manage.py runserver'
	    	}
	    }
    }
  
}