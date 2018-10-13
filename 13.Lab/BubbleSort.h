void bubb(long si, long t[si])
{
	for(long i=0;i<si;i++){
		for(long j=0;j<si;j++){
			if(t[j]>t[j+1]){
				long temporary=t[j];
				t[j]=t[j+1];
				t[j+1]=temporary;
			}
		}
	}
}