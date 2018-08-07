pipeline {
  agent any
  stages {
    stage('Start Postgres server') {
	    steps {
	        sh 'docker start 5bd17760ac74'
	    }

	    steps{
	      	sh 'docker attach 5bd17760ac74'
	    }

	    steps{
	      	sh 'service postgresql restart'
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