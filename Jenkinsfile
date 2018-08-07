pipeline {
  agent any
  stages {
    stage('Start Postgres server') {
	    steps {
	       
            	sh 'docker start 5bd17760ac74'           
            	sh 'docker exec -i reverent_jackson service postgresql restart'
                 
	    }
	}

    stage('Activate venv'){
	    steps{
	    	
            	sh 'cd polls_venv'
                sh '. bin/activate'
            	sh 'cd ..'
      	    }
    }

    stage('Run django server'){
    	steps{
    		sh 'python manage.py runserver'
    	}
    }
  }
}