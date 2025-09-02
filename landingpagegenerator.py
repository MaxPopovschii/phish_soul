import os

LANDING_DIR = 'landings'
os.makedirs(LANDING_DIR, exist_ok=True)

class LandingPageGenerator:
    def generate_twitter_password_reset(self, name):
        html = '''
        <html>
        <head><title>Twitter - Password Reset</title></head>
        <body style="background:#e6ecf0;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.2);">
                <img src="https://abs.twimg.com/icons/apple-touch-icon-192x192.png" width="60" style="display:block;margin:0 auto 20px;">
                <h3 style="text-align:center;">Change Your Password</h3>
                <form>
                    <input type="password" placeholder="Current Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="Confirm New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <button type="submit" style="width:100%;background:#1da1f2;color:#fff;padding:8px;border:none;border-radius:4px;">Change Password</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real Twitter page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_twitter_pwreset.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Twitter password reset clone generated: {path}")

    def generate_linkedin_password_reset(self, name):
        html = '''
        <html>
        <head><title>LinkedIn - Password Reset</title></head>
        <body style="background:#f3f6f8;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.2);">
                <img src="https://static-exp1.licdn.com/sc/h/8w0z7p4g7p6a1t2w6q8p6q8p6" width="60" style="display:block;margin:0 auto 20px;">
                <h3 style="text-align:center;">Change Your Password</h3>
                <form>
                    <input type="password" placeholder="Current Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="Confirm New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <button type="submit" style="width:100%;background:#0077b5;color:#fff;padding:8px;border:none;border-radius:4px;">Change Password</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real LinkedIn page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_linkedin_pwreset.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"LinkedIn password reset clone generated: {path}")

    def generate_tiktok_password_reset(self, name):
        html = '''
        <html>
        <head><title>TikTok - Password Reset</title></head>
        <body style="background:#fff;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.2);">
                <img src="https://s16.tiktokcdn.com/musical/resource/mtact/static/pwa_icon_144.png" width="60" style="display:block;margin:0 auto 20px;">
                <h3 style="text-align:center;">Change Your Password</h3>
                <form>
                    <input type="password" placeholder="Current Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <input type="password" placeholder="Confirm New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ccc;border-radius:4px;"><br>
                    <button type="submit" style="width:100%;background:#010101;color:#fff;padding:8px;border:none;border-radius:4px;">Change Password</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real TikTok page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_tiktok_pwreset.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"TikTok password reset clone generated: {path}")
    def generate_instagram_password_reset(self, name):
        html = '''
        <html>
        <head><title>Instagram - Password Reset</title></head>
        <body style="background:#fafafa;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border:1px solid #dbdbdb;">
                <img src="https://instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" width="175" style="display:block;margin:0 auto 20px;">
                <h3 style="text-align:center;">Change Your Password</h3>
                <form>
                    <input type="password" placeholder="Old Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #dbdbdb;"><br>
                    <input type="password" placeholder="New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #dbdbdb;"><br>
                    <input type="password" placeholder="Confirm New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #dbdbdb;"><br>
                    <button type="submit" style="width:100%;background:#3897f0;color:#fff;padding:8px;border:none;border-radius:4px;">Change Password</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real Instagram page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_insta_pwreset.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Instagram password reset clone generated: {path}")

    def generate_facebook_password_reset(self, name):
        html = '''
        <html>
        <head><title>Facebook - Password Reset</title></head>
        <body style="background:#f0f2f5;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.2);">
                <img src="https://www.facebook.com/images/fb_icon_325x325.png" width="60" style="display:block;margin:0 auto 20px;">
                <h3 style="text-align:center;">Change Your Password</h3>
                <form>
                    <input type="password" placeholder="Current Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ddd;border-radius:4px;"><br>
                    <input type="password" placeholder="New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ddd;border-radius:4px;"><br>
                    <input type="password" placeholder="Confirm New Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ddd;border-radius:4px;"><br>
                    <button type="submit" style="width:100%;background:#1877f2;color:#fff;padding:8px;border:none;border-radius:4px;">Change Password</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real Facebook page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_fb_pwreset.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Facebook password reset clone generated: {path}")
    def generate_instagram_clone(self, name):
        html = '''
        <html>
        <head><title>Instagram</title></head>
        <body style="background:#fafafa;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border:1px solid #dbdbdb;">
                <img src="https://instagram.com/static/images/web/mobile_nav_type_logo.png/735145cfe0a4.png" width="175" style="display:block;margin:0 auto 20px;">
                <form>
                    <input type="text" placeholder="Phone number, username, or email" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #dbdbdb;"><br>
                    <input type="password" placeholder="Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #dbdbdb;"><br>
                    <button type="submit" style="width:100%;background:#3897f0;color:#fff;padding:8px;border:none;border-radius:4px;">Log In</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real Instagram page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_insta.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Instagram clone landing page generated: {path}")

    def generate_facebook_clone(self, name):
        html = '''
        <html>
        <head><title>Facebook</title></head>
        <body style="background:#f0f2f5;font-family:sans-serif;">
            <div style="width:350px;margin:50px auto;padding:40px;background:#fff;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.2);">
                <img src="https://www.facebook.com/images/fb_icon_325x325.png" width="60" style="display:block;margin:0 auto 20px;">
                <form>
                    <input type="text" placeholder="Email or phone number" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ddd;border-radius:4px;"><br>
                    <input type="password" placeholder="Password" style="width:100%;margin-bottom:6px;padding:9px;border:1px solid #ddd;border-radius:4px;"><br>
                    <button type="submit" style="width:100%;background:#1877f2;color:#fff;padding:8px;border:none;border-radius:4px;">Log In</button>
                </form>
                <div style="margin-top:20px;text-align:center;color:#999;">Not real Facebook page. For training only.</div>
            </div>
        </body>
        </html>
        '''
        path = os.path.join(self.landing_dir, f"{name}_fb.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Facebook clone landing page generated: {path}")
    def __init__(self, landing_dir=LANDING_DIR):
        self.landing_dir = landing_dir
        os.makedirs(self.landing_dir, exist_ok=True)

    def generate_landing(self, name, title, message):
        html = f"""
        <html>
        <head><title>{title}</title></head>
        <body>
            <h2>{title}</h2>
            <p>{message}</p>
            <form>
                <input type='text' placeholder='Username'><br>
                <input type='password' placeholder='Password'><br>
                <button type='submit'>Login</button>
            </form>
        </body>
        </html>
        """
        path = os.path.join(self.landing_dir, f"{name}.html")
        with open(path, 'w') as f:
            f.write(html)
        print(f"Landing page generata: {path}")

    def list_landings(self):
        return [f for f in os.listdir(self.landing_dir) if f.endswith('.html')]

    def delete_landing(self, name):
        path = os.path.join(self.landing_dir, f"{name}.html")
        if os.path.exists(path):
            os.remove(path)
            print(f"Landing page '{name}' rimossa.")
        else:
            print(f"Landing page '{name}' non trovata.")
