;Program to display n factorial (iterative)
(defvar prod)	;defines env scope variable
(defun fact (n)
	(setq prod 1) ;function scope var
	(loop for i from 2 to n
		do(setq prod (* prod i)))
	(return-from  fact prod)
)
(defvar n)
(write-line "Enter n:")
(setf n (read))	;setq sets values of symbols only and setf can set anything
(when (< n 0) (write-line "N cannot be less than 0!"))
(when (< n 0) (quit))
(write-line (format nil "~D factorial is :" n))	;second argument specifies stream, nil returns created string
(write (fact n))
(terpri)
