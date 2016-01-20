#!/usr/bin/python

def count_neighbours(grid, row, col):
	rl=len(grid[0])
	cl=len(grid)
	cnt=0
	for i in range(row-1,row+2):
		for j in range(col-1,col+2):
			if(i>=0 and j>=0 and i<rl and j<cl and (i!=row or j!=col)):
				print "%s %s" %(i,j)
				if (grid[i][j]==1):
					cnt+=1
	return cnt

сount_neighbours(((1,0,1,0,1),(0,1,0,1,0),(1,0,1,0,1),(0,1,0,1,0),(1,0,1,0,1),(0,1,0,1,0),),5,4)
