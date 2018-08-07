pipeline {
  agent any
  stages {
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