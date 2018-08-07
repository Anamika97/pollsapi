pipeline {
  agent any
  stages {
    stage('Start Postgres server') {
	    steps {
	        parallel("first": {
                	sh 'docker start 5bd17760ac74'
                },
                "second": {
                    sh 'docker attach 5bd17760ac74'
                },
                "third": {
                	sh 'service postgresql restart'
                }
            )
	    }
	}

    stage('Activate venv'){
	    steps{
	    	parallel("first": {
                	sh 'cd polls_venv'
                },
                "second": {
                    sh '. bin/activate'
                },
                "third": {
                	sh 'cd ..'
                }
            )
	    }
    }

    stage('Run django server'){
    	steps{
    		sh 'python manage.py runserver'
    	}
    }
  }
}