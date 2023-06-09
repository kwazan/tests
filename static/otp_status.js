const checkOtpStatus = (otpId) => {
    fetch(`/check_otp_status/${otpId}`)
    .then(response => response.json())
    .then(data => {
        switch(data.status) {
            case 'APPROVED':
                window.location.href = '/new_page';
                break;
            case 'DECLINED':
                const errorMessage = document.createElement('div');
                errorMessage.innerText = 'Your OTP was declined. Please try again.';
                errorMessage.style.color = 'red';
                document.querySelector('.otp_input').after(errorMessage);
                break;
            default:
                setTimeout(() => checkOtpStatus(otpId), 1000);
        }
    });
};
