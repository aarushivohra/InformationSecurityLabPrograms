import math

# This list maintains the amount by which to rotate the buffers during processing stage
rotate_by = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
			 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
			 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
			 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

# This list maintains the additive constant to be added in each processing step.
constants = [int(abs(math.sin(i+1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]


def pad(msg):
	msg_len_in_bits = (8*len(msg)) & 0xffffffffffffffff
	msg.append(0x80)

	while len(msg)%64 != 56:
		msg.append(0)


	msg += msg_len_in_bits.to_bytes(8, byteorder='little') 
	return msg


init_MDBuffer = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def leftRotate(x, amount):
	x &= 0xFFFFFFFF
	return (x << amount | x >> (32-amount)) & 0xFFFFFFFF


def processMessage(msg):
	init_temp = init_MDBuffer[:] 

	for offset in range(0, len(msg), 64):
		A, B, C, D = init_temp 
		block = msg[offset : offset+64] 
		
		for i in range(64): 
			if i < 16:
				# Round 1
				func = lambda b, c, d: (b & c) | (~b & d)
				# if b is true then ans is c, else d.
				index_func = lambda i: i

			elif i >= 16 and i < 32:
				# Round 2
				func = lambda b, c, d: (d & b) | (~d & c)
				index_func = lambda i: (5*i + 1)%16

			elif i >= 32 and i < 48:
				# Round 3
				func = lambda b, c, d: b ^ c ^ d
				# Parity of b, c, d
				index_func = lambda i: (3*i + 5)%16
			
			elif i >= 48 and i < 64:
				# Round 4
				func = lambda b, c, d: c ^ (b | ~d)
				index_func = lambda i: (7*i)%16

			F = func(B, C, D) # operate on MD Buffers B, C, D
			G = index_func(i) # select one of the 32-bit words from the 512-bit block of the original message to operate on.

			to_rotate = A + F + constants[i] + int.from_bytes(block[4*G : 4*G + 4], byteorder='little')
			newB = (B + leftRotate(to_rotate, rotate_by[i])) & 0xFFFFFFFF
				
			A, B, C, D = D, newB, B, C
			# rotate the contents of the 4 MD buffers by one every pass through the loop

		# Add the final output of the above stage to initial buffer states
		for i, val in enumerate([A, B, C, D]):
			init_temp[i] += val
			init_temp[i] &= 0xFFFFFFFF
		# The init_temp list now holds the MD(in the form of the 4 buffers A, B, C, D) of the 512-bit block of the message fed.

	return sum(buffer_content<<(32*i) for i, buffer_content in enumerate(init_temp))


def MD_to_hex(digest):
	raw = digest.to_bytes(16, byteorder='little')
	return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))


def md5(msg):
	msg = bytearray(msg, 'ascii') # create a copy of the original message in form of a sequence of integers [0, 256)
	msg = pad(msg)
	processed_msg = processMessage(msg)

	message_hash = MD_to_hex(processed_msg)
	print("Message Hash = ", message_hash)



if __name__ == '__main__':
	message = input()
	md5(message)



# reference from https://github.com/Utkarsh87/md5-hashing/blob/master/md5.py
