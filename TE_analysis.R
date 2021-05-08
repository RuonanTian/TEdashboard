TE_gtf<-read.table("D:/working/2019-2020学年/毕设/Data/hg38_rmsk_TE.gtf/hg38_rmsk_TE.gtf",header = FALSE)
TE_copynumber<-as.data.frame(table(TE_gtf$V10))
TE_class<-as.data.frame(table(TE_gtf$V19))
TE_gtf_v1<-TE_gtf[,c(-9,-11,-12,-14,-15,-17,-18,-20)]
colnames(TE_gtf_v1)<-c("seqname","source","feature","start","end","score","strand","frame","gene_id","transcript_id","family_id","class_id")
length<-(TE_gtf_v1$end-TE_gtf_v1$start)
gene_id=TE_gtf_v1$gene_id
transcript_id=TE_gtf_v1$transcript_id
class_id=TE_gtf_v1$class_id
TE_length<-data.frame(gene_id,transcript_id,class_id,length)
TE_length_table<-table(cut(TE_length$length,breaks=seq(1,max(TE_length$length),by=100)))
TE_length_dataframe<-as.data.frame(TE_length_table)
library(ggplot2)
ggplot(data = TE_length,mapping = aes(y=length))+geom_boxplot()
ggplot(data = TE_length,mapping = aes(y=length,x=class_id))+geom_boxplot()+coord_flip()
table(cut(TE_length$length,breaks=c(0,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,500000)))
write.csv(TE_length_dataframe,file="D:/working/2019-2020学年/毕设/Data/TE_length_bins100.csv")
write.csv(TE_copynumber,file="D:/working/2019-2020学年/毕设/Data/TE_copynumber.csv")
write.csv(TE_class,file="D:/working/2019-2020学年/毕设/Data/TE_class.csv")
