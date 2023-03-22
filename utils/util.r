display_info <- function(data){
    str(data)
    cat('-------------------------------------------------------------------------\n')
    summary(data)
}

get_mode <- function(v){
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}

cheak_na <- function(data){
    cat('결측치 원소의 개수:',sum(is.na(data)),'\n')
    cat('결측치를 포함한 행의 수:',sum(!complete.cases(data)),'\n')
}
