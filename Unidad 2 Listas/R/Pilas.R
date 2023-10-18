Pila <- list()
push <- function(pila,elemento){
  pila <- c(pila,elemento)
  return(pila)
}
pop <- function(pila){
  if(length(pila)>0){
    elemento <- pila[length(pila)]
    pila<-pila[-length(pila)]
    return(pila(elemento,pila))
  }else{
    return("La pila está vacía")
  }
}
MiPila <- list()
MiPila <- push(MiPila,0)
elemento <- pop(MiPila)
