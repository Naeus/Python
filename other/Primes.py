def Primes(highRange, *lowRange):

  if len(lowRange) > 1:   return False

  highRange = abs(highRange)
  l = 0
  primes = ()

  if lowRange:
      lowRange[0] = abs(lowRange[0])
      if highRange < lowRange[0]:
          l = highRange
          highRange = lowRange[0]
      else:   l = lowRange[0]

  if l % 2 == 0:
      l = l + 1
      if l <= 2:    primes = primes + (2,)

  primes = primes + tuple(n for n in range(l, highRange + 1, 2) if (2**(n-1) % n) == 1 and n !=341)
  return primes
