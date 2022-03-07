.global__start

.data	
.word  20,23,10,2,5,65,21,45,1

.text 
__start:
	li		$s6,9
	li		$s5,1		
	sub		$t2,$s6,$s5
			
Outerloop:
	beq		$t2,$zero,else3
	li		$t0,0
	li		$a2,0
innerloop:
	beq		$t0,$t2,else4
	j		swap
tag1:
	addi		$a2,$a2,4
	addi		$t0,$t0,1
	j		innerloop

else4: sub		$t2,$t2,$s5
	j		Outerloop		
else3:	j		exit


swap:	li		$a3,0
	lw		$s2,0($a2)
	addi		$a3,$a2,4
	lw		$s3,0($a3)
	blt		$s2,$s3,else5
	j		swapping

else5:	j		tag1


swapping:
	sw		$s2,0($a3)
	sw		$s3,0($a2)
	j		else5

exit:
