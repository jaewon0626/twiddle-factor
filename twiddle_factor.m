% twiddle factor

N = 512;
theta = linspace(0, pi/2, N); % 0부터 π/2까지 N등분하여 각도 생성

for t = 1:N
    W = exp(-1j * theta(t)); % 회전인자 각도 설정
    p(t) = W;
end

r = real(p)'
i = imag(p)'
